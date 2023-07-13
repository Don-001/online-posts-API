"""create votes table

Revision ID: 12270d09aa90
Revises: 49406c9d1cfb
Create Date: 2023-07-13 21:22:23.221673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12270d09aa90'
down_revision = '49406c9d1cfb'
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )


def downgrade() -> None:
    op.drop_table('votes')
