# myapp/management/commands/create_groups_and_permissions.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **kwargs):
        # 创建组
        library_members_group, created = Group.objects.get_or_create(name='Library Members')
        supervisors_group, created = Group.objects.get_or_create(name='Supervisors')
        coordinators_group, created = Group.objects.get_or_create(name='Coordinators')

        # 创建自定义权限
        content_type = ContentType.objects.get_for_model(Permission)

        add_item_permission, created = Permission.objects.get_or_create(
            codename='add_item',
            name='Can add item',
            content_type=content_type,
        )
        edit_item_permission, created = Permission.objects.get_or_create(
            codename='edit_item',
            name='Can edit item',
            content_type=content_type,
        )
        delete_item_permission, created = Permission.objects.get_or_create(
            codename='delete_item',
            name='Can delete item',
            content_type=content_type,
        )

        # 分配权限给组
        library_members_group.permissions.add(add_item_permission)
        supervisors_group.permissions.set([add_item_permission, edit_item_permission])
        coordinators_group.permissions.set([add_item_permission, edit_item_permission, delete_item_permission])

        self.stdout.write(self.style.SUCCESS('Successfully created groups and assigned permissions'))
