"""Renaming students to scholars

Revision ID: eafce7bf5d39
Revises: 791279dd0760
Create Date: 2023-06-02 19:04:59.475261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eafce7bf5d39'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
