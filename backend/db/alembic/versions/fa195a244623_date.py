"""'date'

Revision ID: fa195a244623
Revises: bd08c841f688
Create Date: 2022-05-18 20:42:22.656960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa195a244623'
down_revision = 'bd08c841f688'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('date', sa.Date(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'date')
    # ### end Alembic commands ###
