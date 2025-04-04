import React, {useContext} from "react";
import PropTypes from "prop-types";
import _isEmpty from "lodash/isEmpty";
import Overridable from "react-overridable";
import {withState, ActiveFilters, ResultsPerPage} from "react-searchkit";
import {Container, Grid, Button, Header, Icon} from "semantic-ui-react";
import {i18next as i18nOARepo} from "@translations/oarepo_ui/i18next";
import {i18next} from "@translations/i18next";
import {ShouldActiveFiltersRender, ActiveFiltersCountFloatingLabel, ClearFiltersButton} from "@js/oarepo_ui";
import {
    SearchAppFacets,
    SearchAppResultsPane,
    SearchBar,
    SearchConfigurationContext,
} from "@js/invenio_search_ui/components";
import {ResultOptions} from "@js/invenio_search_ui/components/Results";
import {ResultCountWithState, ResultsPerPageLabel, GridResponsiveSidebarColumn} from "@lter_search";
import {BackToTopButton} from "../../components/BackToTopButton";

const ResultOptionsWithState = withState(ResultOptions);

export const SearchAppLayout = ({config, hasButtonSidebar}) => {
    const [sidebarVisible, setSidebarVisible] = React.useState(false);

    const {appName, buildUID, paginationOptions: {resultsPerPage}} = useContext(SearchConfigurationContext);

    const facetsAvailable = !_isEmpty(config.aggs);

    let columnsAmount;
    let resultsPaneLayoutFacets;

    if (facetsAvailable) {
        if (hasButtonSidebar) {
            columnsAmount = 3;
            resultsPaneLayoutFacets = {
                mobile: 16,
                tablet: 16,
                computer: 10,
                largeScreen: 10,
                widescreen: 10,
                width: undefined,
            };
        } else {
            columnsAmount = 2;
            resultsPaneLayoutFacets = {
                mobile: 16,
                tablet: 16,
                computer: 12,
                largeScreen: 12,
                widescreen: 12,
                width: undefined,
            };
        }
    } else {
        if (hasButtonSidebar) {
            columnsAmount = 2;
            resultsPaneLayoutFacets = {
                mobile: 16,
                tablet: 16,
                computer: 12,
                largeScreen: 12,
                widescreen: 12,
                width: undefined,
            };
        } else {
            columnsAmount = 1;
            resultsPaneLayoutFacets = {
                mobile: 16,
                tablet: 16,
                computer: 16,
                largeScreen: 16,
                widescreen: 16,
                width: undefined,
            };
        }
    }

    const resultsPaneLayoutNoFacets = resultsPaneLayoutFacets;

    // make list full width if no facets available
    const resultsPaneLayout = facetsAvailable
        ? resultsPaneLayoutFacets
        : resultsPaneLayoutNoFacets;

    return (
        <div>
            <Container fluid>
                <Grid
                    columns={columnsAmount}
                    relaxed
                    className="search-app"
                >
                    <Grid.Row>
                        <Grid.Column only="computer" width={4}/>
                        <Grid.Column {...resultsPaneLayout}>
                            <SearchBar buildUID={buildUID} appName={appName}/>

                            {facetsAvailable && (
                                <ShouldActiveFiltersRender>
                                    <ActiveFilters/>
                                </ShouldActiveFiltersRender>
                            )}
                        </Grid.Column>
                    </Grid.Row>
                    <Grid.Row verticalAlign="middle" className="result-options">
                        {facetsAvailable && (
                            <Grid.Column
                                floated="left"
                                only="mobile tablet"
                                mobile={3}
                                tablet={2}
                                textAlign="left"
                                verticalAlign="middle"
                                className="search-burger-sidebar-btn"
                            >
                                <Button
                                    basic
                                    onClick={() => setSidebarVisible(true)}
                                    title={i18next.t("Filter results")}
                                    aria-label={i18next.t("Filter results")}
                                    className="facets-sidebar-open-button"
                                >
                                    <Icon name="filter"/>
                                    <ShouldActiveFiltersRender>
                                        <ActiveFiltersCountFloatingLabel className="bg-carrotOrange"/>
                                    </ShouldActiveFiltersRender>
                                </Button>
                            </Grid.Column>
                        )}
                        <Grid.Column only=" computer" width={4}>
                            {facetsAvailable && (
                                <Grid.Row>
                                    <Header size=" medium"
                                            id=" search-filters-header-title">{i18nOARepo.t(" Filters")}</Header>
                                </Grid.Row>
                            )}
                        </Grid.Column>
                        <Grid.Column {...resultsPaneLayout} mobile={13} tablet={14}>
                            <Grid as={Grid.Row} verticalAlign=" middle">
                                <Grid.Column className=" search-result-count" floated=" left" textAlign=" left"
                                             width={3}>
                                    <ResultCountWithState/>
                                </Grid.Column>
                                <Grid.Column floated="right" textAlign="right" width={13}>
                                    <ResultsPerPage
                                        values={resultsPerPage}
                                        label={ResultsPerPageLabel}
                                    />
                                    <ResultOptionsWithState/>
                                </Grid.Column>
                            </Grid>
                        </Grid.Column>
                    </Grid.Row>
                    <Grid.Row columns={columnsAmount} className=" facets-and-search-listing">
                        {facetsAvailable && (
                            <GridResponsiveSidebarColumn
                                mobile={4}
                                tablet={4}
                                computer={4}
                                largeScreen={4}
                                widescreen={4}
                                open={sidebarVisible}
                                onHideClick={() => setSidebarVisible(false)}
                                mobileChildren={
                                    <>
                                        <ShouldActiveFiltersRender>
                                            <ClearFiltersButton
                                                clearFiltersButtonClassName=" primary mobile tablet only"
                                            />
                                        </ShouldActiveFiltersRender>
                                        <Header size=" medium"
                                                id=" search-filters-header-title">{i18nOARepo.t(" Filters")}</Header>
                                        <SearchAppFacets
                                            aggs={config.aggs}
                                            appName={appName}
                                            buildUID={buildUID}
                                        />
                                    </>
                                }
                            >
                                <SearchAppFacets
                                    aggs={config.aggs}
                                    appName={appName}
                                    buildUID={buildUID}
                                />
                            </GridResponsiveSidebarColumn>
                        )}
                        <Grid.Column {...resultsPaneLayout}>
                            <SearchAppResultsPane
                                layoutOptions={config.layoutOptions}
                                appName={appName}
                                buildUID={buildUID}
                            />
                        </Grid.Column>
                        {hasButtonSidebar && (
                            <Grid.Column
                                mobile={16}
                                tablet={16}
                                computer={4}
                                largeScreen={4}
                                widescreen={4}
                            >
                                <Overridable
                                    id={buildUID(" SearchApp.buttonSidebarContainer", "", appName)}
                                ></Overridable>
                            </Grid.Column>
                        )}
                    </Grid.Row>
                </Grid>
                <BackToTopButton/>
            </Container>
        </div>
    );
};

SearchAppLayout.propTypes = {
    config: PropTypes.shape({
        searchApi: PropTypes.object.isRequired, // same as ReactSearchKit.searchApi
        initialQueryState: PropTypes.shape({
            queryString: PropTypes.string,
            sortBy: PropTypes.string,
            sortOrder: PropTypes.string,
            page: PropTypes.number,
            size: PropTypes.number,
            hiddenParams: PropTypes.array,
            layout: PropTypes.oneOf([" list", " grid"]),
        }),
    }),
};

export default SearchAppLayout;
