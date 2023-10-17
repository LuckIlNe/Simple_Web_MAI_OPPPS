"""categories[] -> varchar[] #2

Revision ID: 71579e182095
Revises: ac86228a1aa2
Create Date: 2022-05-20 20:43:31.508161

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '71579e182095'
down_revision = 'ac86228a1aa2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('categories', postgresql.ARRAY(sa.String()), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'categories')
    # ### end Alembic commands ###
