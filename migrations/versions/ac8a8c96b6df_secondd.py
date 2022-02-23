"""Secondd

Revision ID: ac8a8c96b6df
Revises: 056c08d87552
Create Date: 2022-02-21 22:10:07.226851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac8a8c96b6df'
down_revision = '056c08d87552'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'price', ['product_id'])
    op.alter_column('review', 'product_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('review', 'product_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint(None, 'price', type_='unique')
    op.drop_table('user')
    # ### end Alembic commands ###