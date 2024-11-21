#
# Roles within the workflow:
#
# administrator == administrator for the whole repository
#
# Community roles:
#
# CommunityRole("submitter") == people who can create new records
# CommunityRole("owner")     == person who owns the community
# CommunityMembers()         == member of the community
#
# Synthetic roles:
#
# RecordOwners() == actual owner of the record (person who created it)
#
# Record states:
#
# draft == record is being created
# submitted == record is submitted for approval/publishing but not yet accepted
# published == record is published
# deleting == record is in the process of being deleted (request filed but not yet accepted)
#

from datetime import timedelta

from invenio_records_permissions.generators import AnyUser
from oarepo_communities.services.permissions.generators import (
    CommunityRole,
    PrimaryCommunityRole,
    PrimaryCommunityMembers,
)
from oarepo_communities.services.permissions.policy import CommunityDefaultWorkflowPermissions
from oarepo_requests.services.permissions.generators import IfRequestedBy, RequestActive
from oarepo_runtime.services.permissions.generators import RecordOwners, UserWithRole
from oarepo_workflows import (
    AutoApprove,
    IfInState,
    WorkflowRequest,
    WorkflowRequestEscalation,
    WorkflowRequestPolicy,
    WorkflowTransitions,
)
from oarepo_requests.services.permissions.workflow_policies import RequestBasedWorkflowPermissions


class DefaultWorkflowPermissions(CommunityDefaultWorkflowPermissions):
    can_create = [
        PrimaryCommunityRole("submitter"),
        PrimaryCommunityRole("owner"),
        PrimaryCommunityRole("system"),
        PrimaryCommunityRole("uploader"),
        UserWithRole("administrator"),
    ]

    can_read = [
        RecordOwners(),
        # administrator can see everything
        PrimaryCommunityRole("owner"),
        PrimaryCommunityRole("system"),
        PrimaryCommunityRole("uploader"),
        IfInState(
            "published",
            then_=[AnyUser()],
        ),
    ]

    can_update = [
        IfInState("draft", then_=[
            RecordOwners(),
            PrimaryCommunityRole("system"),
            PrimaryCommunityRole("owner")
        ]),
        IfInState("error", then_=[
            RecordOwners(),
            PrimaryCommunityRole("system"),
            PrimaryCommunityRole("owner")
        ]),
        IfInState("validated", then_=[
            RecordOwners(),
            PrimaryCommunityRole("system"),
            PrimaryCommunityRole("owner")
        ]),
        IfInState("published", then_=[
            PrimaryCommunityRole("system")
        ]),
    ]

    can_delete = [
            PrimaryCommunityRole("system"),
            IfInState("draft", then_=[
                RecordOwners(),
                PrimaryCommunityRole("owner")
            ]),
            IfInState("error", then_=[
                RecordOwners(),
                PrimaryCommunityRole("owner")
            ]),
            IfInState("validated", then_=[
                RecordOwners(),
                PrimaryCommunityRole("owner")
            ]),
            IfInState("running", then_=[
                RecordOwners(),
                PrimaryCommunityRole("owner")
            ]),
            IfInState("published", then_=[
                RecordOwners(),
                PrimaryCommunityRole("owner")
            ]),
    ] + CommunityDefaultWorkflowPermissions.can_delete


class DefaultWorkflowRequests(WorkflowRequestPolicy):
    run_external_workflow = WorkflowRequest(
        requesters=[
            IfInState("draft", then_=[RecordOwners(), PrimaryCommunityRole("owner")]),
            IfInState("error", then_=[RecordOwners(),PrimaryCommunityRole("owner")]),
            IfInState("validated", then_=[RecordOwners(),PrimaryCommunityRole("owner")]),
        ],
        recipients=[
            PrimaryCommunityRole("owner")
            # AutoApprove(),
            # if the requester is the curator of the community, auto approve the request
            # IfRequestedBy(
            #     requesters=PrimaryCommunityRole("curator"),
            #     then_=[AutoApprove()],
            #     else_=[PrimaryCommunityRole("curator"), PrimaryCommunityRole("owner")],
            # )
        ],
        transitions=WorkflowTransitions(
            submitted="running", accepted="validated", declined="error"
        ),
        # if the request is not resolved in 21 days, escalate it to the administrator
        escalations=[
            WorkflowRequestEscalation(
                after=timedelta(days=21), recipients=[UserWithRole("administrator")]
            )
        ],
    )

    publish_draft = WorkflowRequest(
        # if the record is in draft state, the owner or curator can request publishing
        requesters=[
            IfInState("validated", then_=[RecordOwners(), PrimaryCommunityRole("owner")]),
            IfInState("draft", then_=[PrimaryCommunityRole("system")])
        ],
        recipients=[
            AutoApprove(),
            # if the requester is the curator of the community, auto approve the request
            # IfRequestedBy(
            #     requesters=PrimaryCommunityRole("curator"),
            #     then_=[AutoApprove()],
            #     else_=[PrimaryCommunityRole("curator"), PrimaryCommunityRole("owner")],
            # )
        ],
        transitions=WorkflowTransitions(
            submitted="submitted", accepted="published", declined="draft"
        ),
        # if the request is not resolved in 21 days, escalate it to the administrator
        escalations=[
            WorkflowRequestEscalation(
                after=timedelta(days=21), recipients=[UserWithRole("administrator")]
            )
        ],
    )

    edit_published_record = WorkflowRequest(
        requesters=[
            IfInState(
                "published",
                then_=[
                    RecordOwners(),
                    PrimaryCommunityRole("owner"),
                    UserWithRole("administrator"),
                ],
            )
        ],
        # the request is auto-approve, we do not limit the owner of the record to create a new
        # draft version.
        recipients=[AutoApprove()],
    )

    new_version = WorkflowRequest(
        requesters=[
            IfInState(
                "published",
                then_=[
                    RecordOwners(),
                    PrimaryCommunityRole("owner"),
                    UserWithRole("administrator"),
                ],
            )
        ],
        # the request is auto-approve, we do not limit the owner of the record to create a new
        # draft version.
        recipients=[AutoApprove()],
    )

    delete_published_record = WorkflowRequest(
        # if the record is draft, it is covered by the delete permission
        # if published, only the owner or curator can request deleting
        requesters=[
            IfInState(
                "published",
                then_=[
                    RecordOwners(),
                    PrimaryCommunityRole("owner"),
                    UserWithRole("administrator"),
                ],
            )
        ],
        recipients=[
            IfRequestedBy(
                requesters=[
                    PrimaryCommunityRole("owner"),
                    UserWithRole("administrator"),
                ],
                then_=[AutoApprove()],
                else_=[PrimaryCommunityRole("owner")],
            )
        ],
        # the record comes to the state of retracting when the request is submitted. If the request
        # is accepted, the record is deleted, if declined, it is published again.
        transitions=WorkflowTransitions(
            submitted="retracting", declined="published", accepted="deleted"
        ),
        # if the request is not resolved in 21 days, escalate it to the administrator
        escalations=[
            WorkflowRequestEscalation(
                after=timedelta(days=21), recipients=[UserWithRole("administrator")]
            )
        ],
    )

    assign_doi = WorkflowRequest(
        requesters=[
            RecordOwners(),
            PrimaryCommunityRole("owner"),
            UserWithRole("administrator"),
        ],
        recipients=[
            IfRequestedBy(
                requesters=[
                    PrimaryCommunityRole("owner"),
                    UserWithRole("administrator"),
                ],
                then_=[AutoApprove()],
                else_=[PrimaryCommunityRole("owner")],
            )
        ],
        escalations=[
            WorkflowRequestEscalation(
                after=timedelta(days=21), recipients=[UserWithRole("administrator")]
            )
        ],
    )