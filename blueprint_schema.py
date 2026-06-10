# /opt/axentx/cloud-native-blueprints/blueprint_schema.py
from __future__ import annotations
from datetime import datetime
from typing import List, Dict, Optional

from pydantic import BaseModel, Field


class Component(BaseModel):
    """A single infrastructure component (e.g. k8s deployment, RDS instance)."""
    name: str
    type: str                     # e.g. "k8s-deployment", "rds-instance", "s3-bucket"
    config: Dict                 # provider‑specific configuration
    dependencies: List[str] = [] # names of other components this one depends on


class Blueprint(BaseModel):
    """Full blueprint document – versioned and self‑describing."""
    blueprint_id: str
    version: str = "1.0.0"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    components: List[Component]
    metadata: Dict[str, str] = {}

    def bump_version(self) -> None:
        """Simple semantic‑patch bump (1.0.0 → 1.0.1)."""
        major, minor, patch = map(int, self.version.split('.'))
        self.version = f"{major}.{minor}.{patch + 1}"