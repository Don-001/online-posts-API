"""Add foreign key constraint between posts and users table in owner column

Revision ID: 49406c9d1cfb
Revises: 0ecca26d6409
Create Date: 2023-07-13 21:17:17.710194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49406c9d1cfb'
down_revision = '0ecca26d6409'
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
        op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
