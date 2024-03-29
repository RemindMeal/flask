from flask_admin.contrib.sqla.ajax import QueryAjaxModelLoader
from flask_admin.model.ajax import DEFAULT_PAGE_SIZE
from flask_admin.model.filters import BaseFilter
from flask_login import current_user
from sqlalchemy import or_


class MyQueryAjaxModelLoader(QueryAjaxModelLoader):

    def get_list(self, term, offset=0, limit=DEFAULT_PAGE_SIZE):
        query = self.session.query(self.model)

        filters = (field.ilike(u'%%%s%%' % term) for field in self._cached_fields)
        query = query.filter(or_(*filters)).filter(self.model.user == current_user)

        if self.order_by:
            query = query.order_by(self.order_by)

        return query.offset(offset).limit(limit).all()


jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
mois = ["Janvier", u"Février", "Mars", "Avril", "Mai", "Juin", "Juillet", u"Août", "Septembtre", "Octobre"]


def date(value, format='%d/%m/%Y'):
    return "{:s}".format(value.strftime(format))


class RecipeFilter(BaseFilter):
    pass