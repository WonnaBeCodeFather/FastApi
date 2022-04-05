"""create user table

Revision ID: 770f867283fe
Revises: 8c58de911cba
Create Date: 2022-04-04 17:38:28.799083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '770f867283fe'
down_revision = '8c58de911cba'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('password_hash', sa.String(), nullable=False),
                    sa.Column('is_admin', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    pass
