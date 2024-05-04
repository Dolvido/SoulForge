"""
Lifecycle Module
================

This module defines the lifecycle of entities within the SoulForge framework.

Submodules:
    - creation: Handles the creation process of entities.
    - maintenance: Manages the maintenance aspects of entities.
    - destruction: Handles the destruction process of entities.
"""

from .privacy_policy import CreationManager, DestructionManager
from .maintenance import MaintenanceManager
