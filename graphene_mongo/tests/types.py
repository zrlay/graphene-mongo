import models

from graphene.relay import Node

from ..types import MongoengineObjectType


class EditorType(MongoengineObjectType):

    class Meta:
        model = models.Editor


class ArticleType(MongoengineObjectType):

    class Meta:
        model = models.Article


class EmbeddedArticleType(MongoengineObjectType):

    class Meta:
        model = models.EmbeddedArticle


class PlayerType(MongoengineObjectType):

    class Meta:
        model = models.Player


class ReporterType(MongoengineObjectType):

    class Meta:
        model = models.Reporter


class ParentType(MongoengineObjectType):

    class Meta:
        model = models.Parent


class ChildType(MongoengineObjectType):

    class Meta:
        model = models.Child


class ProfessorMetadataType(MongoengineObjectType):

    class Meta:
        model = models.ProfessorMetadata


class ProfessorVectorType(MongoengineObjectType):

    class Meta:
        model = models.ProfessorVector


class ArticleNode(MongoengineObjectType):

    class Meta:
        model = models.Article
        interfaces = (Node,)


class EditorNode(MongoengineObjectType):

    class Meta:
        model = models.Editor
        interfaces = (Node,)


class EmbeddedArticleNode(MongoengineObjectType):

    class Meta:
        model = models.EmbeddedArticle
        interfaces = (Node,)


class PlayerNode(MongoengineObjectType):

    class Meta:
        model = models.Player
        interfaces = (Node,)


class ReporterNode(MongoengineObjectType):

    class Meta:
        model = models.Reporter
        interfaces = (Node,)


class ParentNode(MongoengineObjectType):

    class Meta:
        model = models.Parent
        interfaces = (Node,)


class ChildNode(MongoengineObjectType):

    class Meta:
        model = models.Child
        interfaces = (Node,)


class ChildRegisteredBeforeNode(MongoengineObjectType):

    class Meta:
        model = models.ChildRegisteredBefore
        interfaces = (Node, )


class ParentWithRelationshipNode(MongoengineObjectType):

    class Meta:
        model = models.ParentWithRelationship
        interfaces = (Node, )


class ChildRegisteredAfterNode(MongoengineObjectType):

    class Meta:
        model = models.ChildRegisteredAfter
        interfaces = (Node, )


class ProfessorVectorNode(MongoengineObjectType):

    class Meta:
        model = models.ProfessorVector
        interfaces = (Node, )
