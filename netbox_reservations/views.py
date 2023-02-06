from django.db.models import Count, Subquery, OuterRef

from netbox.views import generic
from extras.models import Tag
from . import filtersets, forms, models, tables


#
# Reservation views
#

class ReservationView(generic.ObjectView):
    queryset = models.Reservation.objects.all()

    permission_required = "netbox_reservations.view_reservation"

    def get_extra_context(self, request, instance):
        table = tables.ReducedClaimTable(instance.claims.all())
        table.configure(request)

        return {
            'claims_table': table,
        }


class ReservationListView(generic.ObjectListView):
    queryset = models.Reservation.objects.annotate(
        claim_count=Count('claims')
    )
    table = tables.ReservationTable
    filterset = filtersets.ReservationFilterSet
    filterset_form = forms.ReservationFilterForm

    permission_required = "netbox_reservations.view_reservation"


class ReservationEditView(generic.ObjectEditView):
    queryset = models.Reservation.objects.all()
    form = forms.ReservationForm

    permission_required = "netbox_reservations.edit_reservation"


class ReservationDeleteView(generic.ObjectDeleteView):
    queryset = models.Reservation.objects.all()

    permission_required = "netbox_reservations.delete_reservation"


#
# Claim views
#

class ClaimView(generic.ObjectView):
    queryset = models.Claim.objects.all()

    permission_required = "netbox_reservations.view_claim"


class ClaimListView(generic.ObjectListView):
    queryset = models.Claim.objects.all()
    table = tables.ClaimTable
    filterset = filtersets.ClaimFilterSet
    filterset_form = forms.ClaimFilterForm

    permission_required = "netbox_reservations.view_claim"


class ClaimEditView(generic.ObjectEditView):
    queryset = models.Claim.objects.all()
    form = forms.ClaimForm

    permission_required = "netbox_reservations.edit_claim"


class ClaimDeleteView(generic.ObjectDeleteView):
    queryset = models.Claim.objects.all()

    permission_required = "netbox_reservations.delete_claim"


#
# Tag overview
#

class TagOverviewListView(generic.ObjectListView):
    queryset = Tag.objects.filter().annotate(
        claim_count=Count('claims')
    ).filter(claim_count=0)
    table = tables.TagOverviewTable

    permission_required = "netbox_reservations.view_tag_overview"
