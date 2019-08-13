# ##### BEGIN GPL LICENSE BLOCK #####
# KeenTools for blender is a blender addon for using KeenTools in Blender.
# Copyright (C) 2019  KeenTools

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ##### END GPL LICENSE BLOCK #####

import bpy
from .. config import Config


# Functions for Custom Attributes perform
def has_custom_attribute(obj, attr_name):
    return attr_name in obj.keys()


def get_custom_attribute(obj, attr_name):
    return obj[attr_name]


def get_safe_custom_attribute(obj, attr_name):
    if has_custom_attribute(obj, attr_name):
        return obj[attr_name]
    else:
        return None


def get_custom_attribute_variants(obj, attr_names):
    for attr in attr_names:
        res = get_safe_custom_attribute(obj, attr)
        if res:
            return res
    return None


def set_custom_attribute(obj, attr_name, val):
    obj[attr_name] = val


def has_keentools_attributes(obj):
    attr_name = Config.version_prop_name[0]
    if has_custom_attribute(obj, attr_name):
        return True
    return False


def set_keentools_version(obj, obj_type, ver):
    attr_name = Config.version_prop_name[0]
    set_custom_attribute(obj, attr_name, Config.addon_version)
    attr_name2 = Config.fb_mod_ver_prop_name[0]
    set_custom_attribute(obj, attr_name2, ver)
    attr_name3 = Config.object_type_prop_name[0]
    set_custom_attribute(obj, attr_name3, obj_type)


def get_attr_variant_named(data, attr_names):
    for attribute in attr_names:
        if attribute in data.keys():
            return data[attribute]
    return None


def get_collection(col_name):
    """ Singleton for collection """
    if col_name in bpy.data.collections:
        return bpy.data.collections[col_name]
    fb_col = bpy.data.collections.new(col_name)
    bpy.context.scene.collection.children.link(fb_col)
    return fb_col


def get_fb_collection():
    fb_col = get_collection(Config.default_FB_COLLECTION_NAME)
    return fb_col


def add_to_fb_collection(obj):
    fb_col = get_fb_collection()
    fb_col.objects.link(obj)
