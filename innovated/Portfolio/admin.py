from django.contrib import admin
# pyrefly: ignore [missing-import]
from .models import (
    BusinessEnquiry, ComplianceLaw, HomePage, DomainCard, AboutPage,
    TeamMember, Service, ServiceFeature, ServicePage, ServiceCard, ServiceCardList
)

@admin.register(BusinessEnquiry)
class BusinessEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'corporate_email', 'company_name', 'enquiry_for', 'created_at')
    list_filter = ('enquiry_for', 'created_at')
    search_fields = ('name', 'corporate_email', 'company_name', 'location')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

@admin.register(ComplianceLaw)
class ComplianceLawAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'official_link')
    list_filter = ('category',)
    search_fields = ('name', 'category', 'key_details')
    ordering = ('category', 'name')

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('hero_title',)
    fieldsets = (
        (None, {
            'fields': ('hero_title', 'hero_subtitle', 'banner_image_url')
        }),
    )

class DomainCardInline(admin.TabularInline):
    model = DomainCard
    extra = 3
    fields = ('title', 'icon_class', 'link_url', 'order')

@admin.register(DomainCard)
class DomainCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'order')
    list_editable = ('order',)
    ordering = ('order',)

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('hero_title',)
    fieldsets = (
        (None, {
            'fields': ('hero_title', 'hero_description', 'mission_text', 'vision_text')
        }),
    )

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order')
    list_editable = ('order',)
    ordering = ('order',)

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 3
    fields = ('text', 'order')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    ordering = ('order',)
    inlines = [ServiceFeatureInline]

class ServiceCardListInline(admin.TabularInline):
    model = ServiceCardList
    extra = 5
    fields = ('text', 'order')

class ServiceCardInline(admin.TabularInline):
    model = ServiceCard
    extra = 3
    fields = ('title', 'icon_class', 'content', 'order')
    inlines = [ServiceCardListInline]

@admin.register(ServicePage)
class ServicePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceCardInline]

@admin.register(ServiceCard)
class ServiceCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_page', 'order')
    list_editable = ('order',)
    ordering = ('order',)
