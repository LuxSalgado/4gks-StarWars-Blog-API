"""empty message

Revision ID: 2ceac25a9aa8
Revises: 5d4f83fbfee1
Create Date: 2021-07-17 15:01:53.748583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ceac25a9aa8'
down_revision = '5d4f83fbfee1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('planets', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('density', sa.String(length=120), nullable=False),
    sa.Column('id_people', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_people'], ['people.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    op.drop_table('people')
    # ### end Alembic commands ###
