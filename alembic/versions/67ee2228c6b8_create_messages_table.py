"""create_messages_table

Revision ID: 67ee2228c6b8
Revises: 91f44b95239d
Create Date: 2023-09-19 08:59:11.710734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67ee2228c6b8'
down_revision: Union[str, None] = '91f44b95239d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'messages',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('created_at', sa.DateTime, default=sa.func.now()),
        sa.Column('status', sa.String, index=True),
        sa.Column('broadcast_id', sa.Integer, sa.ForeignKey('broadcasts.id')),
        sa.Column('client_id', sa.Integer, sa.ForeignKey('clients.id'))
    )

def downgrade() -> None:
    op.drop_table('messages')
