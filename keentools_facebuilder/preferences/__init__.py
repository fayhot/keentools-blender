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

"""
This module contains everything connected with the addon preferences
"""

from .operators import *
from .ui import FBAddonPreferences

CLASSES_TO_REGISTER = (
    OBJECT_OT_InstallLicenseOnline,
    OBJECT_OT_FloatingConnect,
    OBJECT_OT_InstallLicenseOffline,
    OBJECT_OT_CopyHardwareId,
    OBJECT_OT_InstallPkt,
    OBJECT_OT_OpenPktLicensePage,
    OBJECT_OT_InstallFromFilePkt,
    OBJECT_OT_OpenManualInstallPage,
    OBJECT_OT_ShowURL,
    FBAddonPreferences
)
