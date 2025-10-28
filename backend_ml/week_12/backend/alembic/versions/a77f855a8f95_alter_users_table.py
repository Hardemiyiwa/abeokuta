"""alter users table

Revision ID: a77f855a8f95
Revises: 771c7a2adace
Create Date: 2025-10-27 11:24:30.141407

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a77f855a8f95'
down_revision: Union[str, Sequence[str], None] = '771c7a2adace'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
        ALTER TABLE users
    ADD COLUMN gender ENUM('male', 'female') DEFAULT 'male';
""")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
        ALTER TABLE users
    DROP COLUMN gender
""")
    pass
