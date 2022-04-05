"""Add owner columns

Revision ID: fcee016b3fd2
Revises: f35b423d7971
Create Date: 2022-04-04 17:12:35.321943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcee016b3fd2'
down_revision = 'f35b423d7971'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('password_hash', sa.String(), nullable=False),
                    sa.Column('is_admin', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
