"""varchar -> varchar[] #3

Revision ID: 0af47dd7e3c2
Revises: 71579e182095
Create Date: 2022-05-20 22:51:00.512091

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0af47dd7e3c2'
down_revision = '71579e182095'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('authors', postgresql.ARRAY(sa.String()), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'authors')
    # ### end Alembic commands ###
