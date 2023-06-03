"""create post table

Revision ID: 3cc7b9c06da3
Revises: 
Create Date: 2023-05-26 16:47:46.930162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cc7b9c06da3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
