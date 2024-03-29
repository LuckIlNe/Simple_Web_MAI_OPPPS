"""name -> title

Revision ID: f37b3cd62542
Revises: fa195a244623
Create Date: 2022-05-20 20:04:45.362449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f37b3cd62542'
down_revision = 'fa195a244623'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('title', sa.String(), nullable=False))
    op.drop_constraint('articles_name_key', 'articles', type_='unique')
    op.create_unique_constraint(None, 'articles', ['title'])
    op.drop_column('articles', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'articles', type_='unique')
    op.create_unique_constraint('articles_name_key', 'articles', ['name'])
    op.drop_column('articles', 'title')
    # ### end Alembic commands ###
