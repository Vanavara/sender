"""create_broadcasts_table

Revision ID: 91f44b95239d
Revises: 0684d08efca2
Create Date: 2023-09-19 08:58:39.131877

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '91f44b95239d'
down_revision: Union[str, None] = '0684d08efca2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'broadcasts',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('start_time', sa.DateTime, default=sa.func.now()),
        sa.Column('message_text', sa.String),
        sa.Column('client_filter', sa.String),
        sa.Column('end_time', sa.DateTime)
    )

def downgrade() -> None:
    op.drop_table('broadcasts')
