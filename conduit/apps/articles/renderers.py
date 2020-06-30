from conduit.apps.core.renderers import ConduitJSONRenderer


class ArticleJSONRenderer(ConduitJSONRenderer):
    object_label = 'article'
    pagination_object_label = 'articles'
    pagination_count_label = 'articlesCount'
