# Copyright (C) 2013 Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Volume ACL permission interface (1.1 extension).
"""

from cinderclient import base


class VolumeACLPermission(base.Resource):
    """Volume ACL permission."""
    def __repr__(self):
        return "<VolumeACLPermission: %s>" % self.id

    def delete(self):
        """Delete this volume permission."""
        return self.manager.delete(self)


class VolumeACLPermissionManager(base.ManagerWithFind):
    """Manage :class:`VolumeACLPermission` resources."""
    resource_class = VolumeACLPermission

    def create(self, volume_id, type, entity_id, access_permission):
        """Create a volume permission.

        :param volume_id: The ID of the volume permission.
        :param type: entity type.
        :param entity_id: The ID of the user or the group.
        :param access_permission: access permission number.
        :rtype: :class:`VolumeACLPermission`
        """
        body = {'volume_acl_permission':
                {'volume_id': volume_id,
                 'type': type,
                 'entity_id': entity_id,
                 'access_permission': access_permission,
                 }
                }
        return self._create('/os-volume-acl', body, 'volume_acl_permission')

    def get(self, volume_permission_id):
        """Show details of a volume permission.

        :param volume_permission_id: The ID of the volume permission to display
        :rtype: :class:`VolumeACLPermission`
        """
        return self._get("/os-volume-acl/%s" % volume_permission_id,
                         "volume_acl_permission")

    def get_access(self, volume_id):
        """Get volume permission.
        :param volume_id: the ID of the volume.
        :rtype: :class:`VolumeACLPermission`
        """
        return self._get("/os-volume-acl/access?volume_id=%s" % volume_id,
                         "volume_acl_permission")

    def get_all_by_volume(self, volume_id, detailed=True):
        """Get a list of all volume permissions for a volume.

        :param volume_id: The ID of the volume
        :rtype: list of :class:`VolumeACLPermission`
        """
        if detailed is True:
            return self._list("/os-volume-acl/detail?volume_id=%s" % volume_id,
                              "volume_acl_permissions")
        else:
            return self._list("/os-volume-acl/?volume_id=%s" % volume_id,
                              "volume_acl_permissions")

    def list(self, detailed=True):
        """Get a list of all volume permissions.

        :rtype: list of :class:`VolumeACLPermission`
        """
        if detailed is True:
            return self._list("/os-volume-acl/detail",
                              "volume_acl_permissions")
        else:
            return self._list("/os-volume-acl",
                              "volume_acl_permissions")

    def delete(self, volume_permission_id):
        """Delete a volume permission.

        :param volume_permission_id: The :class:`VolumeACLPermission` to delete
        """
        self._delete("/os-volume-acl/%s" %
                     base.getid(volume_permission_id))
