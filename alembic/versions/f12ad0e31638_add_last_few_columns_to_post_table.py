"""add last few columns to post table

Revision ID: f12ad0e31638
Revises: 09bc1aa88b76
Create Date: 2023-05-29 00:24:24.063590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f12ad0e31638'
down_revision = '09bc1aa88b76'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_time',
                                     sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_time')

