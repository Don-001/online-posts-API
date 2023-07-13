"""create users table

Revision ID: 0ecca26d6409
Revises: fbb13f7b3ff5
Create Date: 2023-07-13 21:13:08.962662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ecca26d6409'
down_revision = 'fbb13f7b3ff5'
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade() -> None:
    op.drop_table('users')
