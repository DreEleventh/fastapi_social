"""Add user table.

Revision ID: 2be7f4946e9b
Revises: 0fc152674181
Create Date: 2023-05-27 16:43:10.442409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2be7f4946e9b'
down_revision = '0fc152674181'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_time', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade() -> None:
    op.drop_table('users')
