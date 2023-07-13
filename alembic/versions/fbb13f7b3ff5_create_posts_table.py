"""create posts table

Revision ID: fbb13f7b3ff5
Revises: 
Create Date: 2023-07-13 20:35:49.864613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbb13f7b3ff5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False), sa.Column('content', sa.String(), nullable=False), sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))



def downgrade() -> None:
    op.drop_table('posts')
