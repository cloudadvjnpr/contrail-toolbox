
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

from contrail_heat.resources import contrail
try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
from heat.engine import constraints
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
import uuid

from vnc_api import vnc_api

LOG = logging.getLogger(__name__)


class ContrailLoadbalancerHealthmonitor(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, LOADBALANCER_HEALTHMONITOR_PROPERTIES, LOADBALANCER_HEALTHMONITOR_PROPERTIES_ADMIN_STATE, LOADBALANCER_HEALTHMONITOR_PROPERTIES_MONITOR_TYPE, LOADBALANCER_HEALTHMONITOR_PROPERTIES_DELAY, LOADBALANCER_HEALTHMONITOR_PROPERTIES_TIMEOUT, LOADBALANCER_HEALTHMONITOR_PROPERTIES_MAX_RETRIES, LOADBALANCER_HEALTHMONITOR_PROPERTIES_HTTP_METHOD, LOADBALANCER_HEALTHMONITOR_PROPERTIES_URL_PATH, LOADBALANCER_HEALTHMONITOR_PROPERTIES_EXPECTED_CODES, DISPLAY_NAME, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, TAG_REFS, PROJECT
    ) = (
        'name', 'fq_name', 'loadbalancer_healthmonitor_properties', 'loadbalancer_healthmonitor_properties_admin_state', 'loadbalancer_healthmonitor_properties_monitor_type', 'loadbalancer_healthmonitor_properties_delay', 'loadbalancer_healthmonitor_properties_timeout', 'loadbalancer_healthmonitor_properties_max_retries', 'loadbalancer_healthmonitor_properties_http_method', 'loadbalancer_healthmonitor_properties_url_path', 'loadbalancer_healthmonitor_properties_expected_codes', 'display_name', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'tag_refs', 'project'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('NAME.'),
            update_allowed=True,
            required=False,
        ),
        FQ_NAME: properties.Schema(
            properties.Schema.STRING,
            _('FQ_NAME.'),
            update_allowed=True,
            required=False,
        ),
        LOADBALANCER_HEALTHMONITOR_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('LOADBALANCER_HEALTHMONITOR_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_ADMIN_STATE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_ADMIN_STATE.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_MONITOR_TYPE: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_MONITOR_TYPE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'PING', u'TCP', u'HTTP', u'HTTPS']),
                    ],
                ),
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_DELAY: properties.Schema(
                    properties.Schema.INTEGER,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_DELAY.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_TIMEOUT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_TIMEOUT.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_MAX_RETRIES: properties.Schema(
                    properties.Schema.INTEGER,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_MAX_RETRIES.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_HTTP_METHOD: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_HTTP_METHOD.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_URL_PATH: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_URL_PATH.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_EXPECTED_CODES: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_EXPECTED_CODES.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        ANNOTATIONS: properties.Schema(
            properties.Schema.MAP,
            _('ANNOTATIONS.'),
            update_allowed=True,
            required=False,
            schema={
                ANNOTATIONS_KEY_VALUE_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('ANNOTATIONS_KEY_VALUE_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            ANNOTATIONS_KEY_VALUE_PAIR_KEY: properties.Schema(
                                properties.Schema.STRING,
                                _('ANNOTATIONS_KEY_VALUE_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            ANNOTATIONS_KEY_VALUE_PAIR_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('ANNOTATIONS_KEY_VALUE_PAIR_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        PERMS2: properties.Schema(
            properties.Schema.MAP,
            _('PERMS2.'),
            update_allowed=True,
            required=False,
            schema={
                PERMS2_OWNER: properties.Schema(
                    properties.Schema.STRING,
                    _('PERMS2_OWNER.'),
                    update_allowed=True,
                    required=False,
                ),
                PERMS2_OWNER_ACCESS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PERMS2_OWNER_ACCESS.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 7),
                    ],
                ),
                PERMS2_GLOBAL_ACCESS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PERMS2_GLOBAL_ACCESS.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 7),
                    ],
                ),
                PERMS2_SHARE: properties.Schema(
                    properties.Schema.LIST,
                    _('PERMS2_SHARE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            PERMS2_SHARE_TENANT: properties.Schema(
                                properties.Schema.STRING,
                                _('PERMS2_SHARE_TENANT.'),
                                update_allowed=True,
                                required=False,
                            ),
                            PERMS2_SHARE_TENANT_ACCESS: properties.Schema(
                                properties.Schema.INTEGER,
                                _('PERMS2_SHARE_TENANT_ACCESS.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.Range(0, 7),
                                ],
                            ),
                        }
                    )
                ),
            }
        ),
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        PROJECT: properties.Schema(
            properties.Schema.STRING,
            _('PROJECT.'),
            update_allowed=True,
            required=False,
        ),
    }

    attributes_schema = {
        NAME: attributes.Schema(
            _('NAME.'),
        ),
        FQ_NAME: attributes.Schema(
            _('FQ_NAME.'),
        ),
        LOADBALANCER_HEALTHMONITOR_PROPERTIES: attributes.Schema(
            _('LOADBALANCER_HEALTHMONITOR_PROPERTIES.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        PROJECT: attributes.Schema(
            _('PROJECT.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.PROJECT) and self.properties.get(self.PROJECT) != 'config-root':
            try:
                parent_obj = self.vnc_lib().project_read(fq_name_str=self.properties.get(self.PROJECT))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(self.properties.get(self.PROJECT))))
            except:
                parent_obj = None

        if parent_obj is None and self.properties.get(self.PROJECT) != 'config-root':
            tenant_id = self.stack.context.tenant_id
            parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))

        if parent_obj is None and self.properties.get(self.PROJECT) != 'config-root':
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.LoadbalancerHealthmonitor(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES) is not None:
            obj_1 = vnc_api.LoadbalancerHealthmonitorType()
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_ADMIN_STATE))
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MONITOR_TYPE) is not None:
                obj_1.set_monitor_type(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MONITOR_TYPE))
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_DELAY) is not None:
                obj_1.set_delay(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_DELAY))
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_TIMEOUT) is not None:
                obj_1.set_timeout(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_TIMEOUT))
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MAX_RETRIES) is not None:
                obj_1.set_max_retries(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MAX_RETRIES))
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_HTTP_METHOD) is not None:
                obj_1.set_http_method(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_HTTP_METHOD))
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_URL_PATH) is not None:
                obj_1.set_url_path(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_URL_PATH))
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_EXPECTED_CODES) is not None:
                obj_1.set_expected_codes(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_EXPECTED_CODES))
            obj_0.set_loadbalancer_healthmonitor_properties(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.ANNOTATIONS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY))
                    if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_annotations(obj_1)
        if self.properties.get(self.PERMS2) is not None:
            obj_1 = vnc_api.PermType2()
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER) is not None:
                obj_1.set_owner(self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER_ACCESS) is not None:
                obj_1.set_owner_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER_ACCESS))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_GLOBAL_ACCESS) is not None:
                obj_1.set_global_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_GLOBAL_ACCESS))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE) is not None:
                for index_1 in range(len(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE))):
                    obj_2 = vnc_api.ShareType()
                    if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT) is not None:
                        obj_2.set_tenant(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT))
                    if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT_ACCESS) is not None:
                        obj_2.set_tenant_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT_ACCESS))
                    obj_1.add_share(obj_2)
            obj_0.set_perms2(obj_1)

        # reference to tag_refs
        if self.properties.get(self.TAG_REFS):
            for index_0 in range(len(self.properties.get(self.TAG_REFS))):
                try:
                    ref_obj = self.vnc_lib().tag_read(
                        id=self.properties.get(self.TAG_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().tag_read(
                        fq_name_str=self.properties.get(self.TAG_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_tag(ref_obj)

        try:
            obj_uuid = super(ContrailLoadbalancerHealthmonitor, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().loadbalancer_healthmonitor_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES) is not None:
            obj_1 = vnc_api.LoadbalancerHealthmonitorType()
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_ADMIN_STATE))
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MONITOR_TYPE) is not None:
                obj_1.set_monitor_type(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MONITOR_TYPE))
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_DELAY) is not None:
                obj_1.set_delay(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_DELAY))
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_TIMEOUT) is not None:
                obj_1.set_timeout(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_TIMEOUT))
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MAX_RETRIES) is not None:
                obj_1.set_max_retries(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MAX_RETRIES))
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_HTTP_METHOD) is not None:
                obj_1.set_http_method(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_HTTP_METHOD))
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_URL_PATH) is not None:
                obj_1.set_url_path(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_URL_PATH))
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_EXPECTED_CODES) is not None:
                obj_1.set_expected_codes(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_EXPECTED_CODES))
            obj_0.set_loadbalancer_healthmonitor_properties(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.ANNOTATIONS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY))
                    if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_annotations(obj_1)

        # reference to tag_refs
        ref_obj_list = []
        if self.TAG_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.TAG_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().tag_read(
                        id=prop_diff.get(self.TAG_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().tag_read(
                        fq_name_str=prop_diff.get(self.TAG_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_tag_list(ref_obj_list)
            # End: reference to tag_refs

        try:
            self.vnc_lib().loadbalancer_healthmonitor_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().loadbalancer_healthmonitor_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('loadbalancer_healthmonitor %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().loadbalancer_healthmonitor_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::LoadbalancerHealthmonitor': ContrailLoadbalancerHealthmonitor,
    }
