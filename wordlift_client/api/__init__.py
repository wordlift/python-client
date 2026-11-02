# flake8: noqa

__all__ = [
    "AccountApi",
    "AccountChunksetsApi",
    "AccountGraphKPIsApi",
    "AccountStatsApi",
    "AccountsApi",
    "AddOnsApi",
    "AgentApi",
    "AnalysesApi",
    "AnalyticsImportsApi",
    "AnalyticsSyncsApi",
    "AuditApi",
    "AuthorsApi",
    "AutocompleteApi",
    "BotifyCrawlImportsApi",
    "ClassificationsApi",
    "ContentEvaluationsApi",
    "ContentExpansionsApi",
    "ContentGenerationCompletionApi",
    "ContentGenerationFieldsApi",
    "ContentGenerationModelsApi",
    "ContentGenerationPresetsApi",
    "ContentGenerationRecordsApi",
    "ContentGenerationRecordsExportApi",
    "ContentGenerationRendersApi",
    "ContentGenerationStatsApi",
    "ContentGenerationSyncsApi",
    "ContentGenerationWordBiasesApi",
    "ContentGenerationsApi",
    "CustomDomainsApi",
    "DataURIApi",
    "DatasetApi",
    "EmbeddingApi",
    "EmbeddingsApi",
    "EntitiesApi",
    "EntityGapsApi",
    "ExpectationSummaryApi",
    "ExpectationsApi",
    "FactCheckApi",
    "FetchApi",
    "GoogleMerchantsApi",
    "GoogleSearchConsoleApi",
    "GoogleSearchConsoleSearchesApi",
    "GraphQLApi",
    "IncludeExcludesApi",
    "InspectorApi",
    "InternalLinksApi",
    "LinkGroupsApi",
    "LongTailsApi",
    "MerchantSyncsApi",
    "MerchantsApi",
    "MicrodataApi",
    "MonitorCheckSummaryApi",
    "MonitorChecksApi",
    "MonitorRunsApi",
    "MonitorStatusApi",
    "MonitoringSummaryApi",
    "MonitorsApi",
    "OAuth2AuthorizedClientsApi",
    "PagesExplorerApi",
    "PlatformConsumptionsApi",
    "PlatformLimitsApi",
    "PluginDiagnosticsApi",
    "PluginEventsApi",
    "QueryFanOutApi",
    "QuestionAndAnswerSetsApi",
    "QuestionsAndAnswersApi",
    "RedeemCodesApi",
    "ResolveApi",
    "RulesApi",
    "SegmentGlobsApi",
    "SegmentURLsApi",
    "SegmentsApi",
    "SitemapGeneratorApi",
    "SitemapImportsApi",
    "SmartContentsApi",
    "SubscriptionsApi",
    "SummarizationsApi",
    "TokensApi",
    "VectorSearchNodesApi",
    "VectorSearchQueriesApi",
    "WebAsyncsMetadataApi",
    "WebAsyncsResponsesApi",
    "WebPageScrapeApi",
    "WebPagesImportsApi",
    "WebPagesApi",
    "AccountConnectorFieldControllerApi",
    "AccountOAuth2ConnectorControllerApi",
    "BootstrapApi",
    "DefaultApi",
    "FailuresApi",
    "GraphSyncControllerApi",
    "JobsApi",
    "KpisApi",
    "OAuth2ConnectorControllerApi",
    "RunsApi",
    "SnapshotsApi",
]

import typing as _typing

if _typing.TYPE_CHECKING:
    # import apis into api package
    from wordlift_client.api.account_api import AccountApi
    from wordlift_client.api.account_chunksets_api import AccountChunksetsApi
    from wordlift_client.api.account_graph_kpis_api import AccountGraphKPIsApi
    from wordlift_client.api.account_stats_api import AccountStatsApi
    from wordlift_client.api.accounts_api import AccountsApi
    from wordlift_client.api.add_ons_api import AddOnsApi
    from wordlift_client.api.agent_api import AgentApi
    from wordlift_client.api.analyses_api import AnalysesApi
    from wordlift_client.api.analytics_imports_api import AnalyticsImportsApi
    from wordlift_client.api.analytics_syncs_api import AnalyticsSyncsApi
    from wordlift_client.api.audit_api import AuditApi
    from wordlift_client.api.authors_api import AuthorsApi
    from wordlift_client.api.autocomplete_api import AutocompleteApi
    from wordlift_client.api.botify_crawl_imports_api import BotifyCrawlImportsApi
    from wordlift_client.api.classifications_api import ClassificationsApi
    from wordlift_client.api.content_evaluations_api import ContentEvaluationsApi
    from wordlift_client.api.content_expansions_api import ContentExpansionsApi
    from wordlift_client.api.content_generation_completion_api import ContentGenerationCompletionApi
    from wordlift_client.api.content_generation_fields_api import ContentGenerationFieldsApi
    from wordlift_client.api.content_generation_models_api import ContentGenerationModelsApi
    from wordlift_client.api.content_generation_presets_api import ContentGenerationPresetsApi
    from wordlift_client.api.content_generation_records_api import ContentGenerationRecordsApi
    from wordlift_client.api.content_generation_records_export_api import ContentGenerationRecordsExportApi
    from wordlift_client.api.content_generation_renders_api import ContentGenerationRendersApi
    from wordlift_client.api.content_generation_stats_api import ContentGenerationStatsApi
    from wordlift_client.api.content_generation_syncs_api import ContentGenerationSyncsApi
    from wordlift_client.api.content_generation_word_biases_api import ContentGenerationWordBiasesApi
    from wordlift_client.api.content_generations_api import ContentGenerationsApi
    from wordlift_client.api.custom_domains_api import CustomDomainsApi
    from wordlift_client.api.data_uri_api import DataURIApi
    from wordlift_client.api.dataset_api import DatasetApi
    from wordlift_client.api.embedding_api import EmbeddingApi
    from wordlift_client.api.embeddings_api import EmbeddingsApi
    from wordlift_client.api.entities_api import EntitiesApi
    from wordlift_client.api.entity_gaps_api import EntityGapsApi
    from wordlift_client.api.expectation_summary_api import ExpectationSummaryApi
    from wordlift_client.api.expectations_api import ExpectationsApi
    from wordlift_client.api.fact_check_api import FactCheckApi
    from wordlift_client.api.fetch_api import FetchApi
    from wordlift_client.api.google_merchants_api import GoogleMerchantsApi
    from wordlift_client.api.google_search_console_api import GoogleSearchConsoleApi
    from wordlift_client.api.google_search_console_searches_api import GoogleSearchConsoleSearchesApi
    from wordlift_client.api.graph_ql_api import GraphQLApi
    from wordlift_client.api.include_excludes_api import IncludeExcludesApi
    from wordlift_client.api.inspector_api import InspectorApi
    from wordlift_client.api.internal_links_api import InternalLinksApi
    from wordlift_client.api.link_groups_api import LinkGroupsApi
    from wordlift_client.api.long_tails_api import LongTailsApi
    from wordlift_client.api.merchant_syncs_api import MerchantSyncsApi
    from wordlift_client.api.merchants_api import MerchantsApi
    from wordlift_client.api.microdata_api import MicrodataApi
    from wordlift_client.api.monitor_check_summary_api import MonitorCheckSummaryApi
    from wordlift_client.api.monitor_checks_api import MonitorChecksApi
    from wordlift_client.api.monitor_runs_api import MonitorRunsApi
    from wordlift_client.api.monitor_status_api import MonitorStatusApi
    from wordlift_client.api.monitoring_summary_api import MonitoringSummaryApi
    from wordlift_client.api.monitors_api import MonitorsApi
    from wordlift_client.api.o_auth2_authorized_clients_api import OAuth2AuthorizedClientsApi
    from wordlift_client.api.pages_explorer_api import PagesExplorerApi
    from wordlift_client.api.platform_consumptions_api import PlatformConsumptionsApi
    from wordlift_client.api.platform_limits_api import PlatformLimitsApi
    from wordlift_client.api.plugin_diagnostics_api import PluginDiagnosticsApi
    from wordlift_client.api.plugin_events_api import PluginEventsApi
    from wordlift_client.api.query_fan_out_api import QueryFanOutApi
    from wordlift_client.api.question_and_answer_sets_api import QuestionAndAnswerSetsApi
    from wordlift_client.api.questions_and_answers_api import QuestionsAndAnswersApi
    from wordlift_client.api.redeem_codes_api import RedeemCodesApi
    from wordlift_client.api.resolve_api import ResolveApi
    from wordlift_client.api.rules_api import RulesApi
    from wordlift_client.api.segment_globs_api import SegmentGlobsApi
    from wordlift_client.api.segment_urls_api import SegmentURLsApi
    from wordlift_client.api.segments_api import SegmentsApi
    from wordlift_client.api.sitemap_generator_api import SitemapGeneratorApi
    from wordlift_client.api.sitemap_imports_api import SitemapImportsApi
    from wordlift_client.api.smart_contents_api import SmartContentsApi
    from wordlift_client.api.subscriptions_api import SubscriptionsApi
    from wordlift_client.api.summarizations_api import SummarizationsApi
    from wordlift_client.api.tokens_api import TokensApi
    from wordlift_client.api.vector_search_nodes_api import VectorSearchNodesApi
    from wordlift_client.api.vector_search_queries_api import VectorSearchQueriesApi
    from wordlift_client.api.web_asyncs_metadata_api import WebAsyncsMetadataApi
    from wordlift_client.api.web_asyncs_responses_api import WebAsyncsResponsesApi
    from wordlift_client.api.web_page_scrape_api import WebPageScrapeApi
    from wordlift_client.api.web_pages_imports_api import WebPagesImportsApi
    from wordlift_client.api.web_pages_api import WebPagesApi
    from wordlift_client.api.account_connector_field_controller_api import AccountConnectorFieldControllerApi
    from wordlift_client.api.account_o_auth2_connector_controller_api import AccountOAuth2ConnectorControllerApi
    from wordlift_client.api.bootstrap_api import BootstrapApi
    from wordlift_client.api.default_api import DefaultApi
    from wordlift_client.api.failures_api import FailuresApi
    from wordlift_client.api.graph_sync_controller_api import GraphSyncControllerApi
    from wordlift_client.api.jobs_api import JobsApi
    from wordlift_client.api.kpis_api import KpisApi
    from wordlift_client.api.o_auth2_connector_controller_api import OAuth2ConnectorControllerApi
    from wordlift_client.api.runs_api import RunsApi
    from wordlift_client.api.snapshots_api import SnapshotsApi
    
else:
    from importlib import import_module

    _exports = {
        "AccountApi": ".account_api",
        "AccountChunksetsApi": ".account_chunksets_api",
        "AccountGraphKPIsApi": ".account_graph_kpis_api",
        "AccountStatsApi": ".account_stats_api",
        "AccountsApi": ".accounts_api",
        "AddOnsApi": ".add_ons_api",
        "AgentApi": ".agent_api",
        "AnalysesApi": ".analyses_api",
        "AnalyticsImportsApi": ".analytics_imports_api",
        "AnalyticsSyncsApi": ".analytics_syncs_api",
        "AuditApi": ".audit_api",
        "AuthorsApi": ".authors_api",
        "AutocompleteApi": ".autocomplete_api",
        "BotifyCrawlImportsApi": ".botify_crawl_imports_api",
        "ClassificationsApi": ".classifications_api",
        "ContentEvaluationsApi": ".content_evaluations_api",
        "ContentExpansionsApi": ".content_expansions_api",
        "ContentGenerationCompletionApi": ".content_generation_completion_api",
        "ContentGenerationFieldsApi": ".content_generation_fields_api",
        "ContentGenerationModelsApi": ".content_generation_models_api",
        "ContentGenerationPresetsApi": ".content_generation_presets_api",
        "ContentGenerationRecordsApi": ".content_generation_records_api",
        "ContentGenerationRecordsExportApi": ".content_generation_records_export_api",
        "ContentGenerationRendersApi": ".content_generation_renders_api",
        "ContentGenerationStatsApi": ".content_generation_stats_api",
        "ContentGenerationSyncsApi": ".content_generation_syncs_api",
        "ContentGenerationWordBiasesApi": ".content_generation_word_biases_api",
        "ContentGenerationsApi": ".content_generations_api",
        "CustomDomainsApi": ".custom_domains_api",
        "DataURIApi": ".data_uri_api",
        "DatasetApi": ".dataset_api",
        "EmbeddingApi": ".embedding_api",
        "EmbeddingsApi": ".embeddings_api",
        "EntitiesApi": ".entities_api",
        "EntityGapsApi": ".entity_gaps_api",
        "ExpectationSummaryApi": ".expectation_summary_api",
        "ExpectationsApi": ".expectations_api",
        "FactCheckApi": ".fact_check_api",
        "FetchApi": ".fetch_api",
        "GoogleMerchantsApi": ".google_merchants_api",
        "GoogleSearchConsoleApi": ".google_search_console_api",
        "GoogleSearchConsoleSearchesApi": ".google_search_console_searches_api",
        "GraphQLApi": ".graph_ql_api",
        "IncludeExcludesApi": ".include_excludes_api",
        "InspectorApi": ".inspector_api",
        "InternalLinksApi": ".internal_links_api",
        "LinkGroupsApi": ".link_groups_api",
        "LongTailsApi": ".long_tails_api",
        "MerchantSyncsApi": ".merchant_syncs_api",
        "MerchantsApi": ".merchants_api",
        "MicrodataApi": ".microdata_api",
        "MonitorCheckSummaryApi": ".monitor_check_summary_api",
        "MonitorChecksApi": ".monitor_checks_api",
        "MonitorRunsApi": ".monitor_runs_api",
        "MonitorStatusApi": ".monitor_status_api",
        "MonitoringSummaryApi": ".monitoring_summary_api",
        "MonitorsApi": ".monitors_api",
        "OAuth2AuthorizedClientsApi": ".o_auth2_authorized_clients_api",
        "PagesExplorerApi": ".pages_explorer_api",
        "PlatformConsumptionsApi": ".platform_consumptions_api",
        "PlatformLimitsApi": ".platform_limits_api",
        "PluginDiagnosticsApi": ".plugin_diagnostics_api",
        "PluginEventsApi": ".plugin_events_api",
        "QueryFanOutApi": ".query_fan_out_api",
        "QuestionAndAnswerSetsApi": ".question_and_answer_sets_api",
        "QuestionsAndAnswersApi": ".questions_and_answers_api",
        "RedeemCodesApi": ".redeem_codes_api",
        "ResolveApi": ".resolve_api",
        "RulesApi": ".rules_api",
        "SegmentGlobsApi": ".segment_globs_api",
        "SegmentURLsApi": ".segment_urls_api",
        "SegmentsApi": ".segments_api",
        "SitemapGeneratorApi": ".sitemap_generator_api",
        "SitemapImportsApi": ".sitemap_imports_api",
        "SmartContentsApi": ".smart_contents_api",
        "SubscriptionsApi": ".subscriptions_api",
        "SummarizationsApi": ".summarizations_api",
        "TokensApi": ".tokens_api",
        "VectorSearchNodesApi": ".vector_search_nodes_api",
        "VectorSearchQueriesApi": ".vector_search_queries_api",
        "WebAsyncsMetadataApi": ".web_asyncs_metadata_api",
        "WebAsyncsResponsesApi": ".web_asyncs_responses_api",
        "WebPageScrapeApi": ".web_page_scrape_api",
        "WebPagesImportsApi": ".web_pages_imports_api",
        "WebPagesApi": ".web_pages_api",
        "AccountConnectorFieldControllerApi": ".account_connector_field_controller_api",
        "AccountOAuth2ConnectorControllerApi": ".account_o_auth2_connector_controller_api",
        "BootstrapApi": ".bootstrap_api",
        "DefaultApi": ".default_api",
        "FailuresApi": ".failures_api",
        "GraphSyncControllerApi": ".graph_sync_controller_api",
        "JobsApi": ".jobs_api",
        "KpisApi": ".kpis_api",
        "OAuth2ConnectorControllerApi": ".o_auth2_connector_controller_api",
        "RunsApi": ".runs_api",
        "SnapshotsApi": ".snapshots_api",
    }

    def __getattr__(name: str) -> object:
        if (module_name := _exports.get(name)) is None:
            raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
        value = getattr(import_module(module_name, __name__), name)
        globals()[name] = value
        return value

    def __dir__() -> list[str]:
        return sorted(globals().keys() | _exports.keys())
