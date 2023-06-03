"""add published, created_time and owner_id (the foreign key) to the post table

Revision ID: 09bc1aa88b76
Revises: 2be7f4946e9b
Create Date: 2023-05-28 13:36:18.772909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09bc1aa88b76'
down_revision = '2be7f4946e9b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts",
                          referent_table='users', local_cols=['owner_id'],
                          remote_cols=['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
