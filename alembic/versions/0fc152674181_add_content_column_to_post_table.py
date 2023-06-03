"""add content column to post table

Revision ID: 0fc152674181
Revises: 3cc7b9c06da3
Create Date: 2023-05-26 18:13:47.662038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fc152674181'
down_revision = '3cc7b9c06da3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
