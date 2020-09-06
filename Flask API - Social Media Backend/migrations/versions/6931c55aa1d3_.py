"""empty message

Revision ID: 6931c55aa1d3
Revises: d8ec6c92893e
Create Date: 2020-08-25 03:16:43.004910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6931c55aa1d3'
down_revision = 'd8ec6c92893e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('cards_title_key', 'cards', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('cards_title_key', 'cards', ['title'])
    # ### end Alembic commands ###
