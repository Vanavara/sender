"""create_client_table

Revision ID: 0684d08efca2
Revises: 
Create Date: 2023-09-19 08:57:33.459734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0684d08efca2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'clients',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('phone_number', sa.String, unique=True),
        sa.Column('operator_code', sa.String, nullable=True),
        sa.Column('tag', sa.String, nullable=True),
        sa.Column('timezone', sa.String, nullable=True)
    )


def downgrade() -> None:
    op.drop_table('clients')