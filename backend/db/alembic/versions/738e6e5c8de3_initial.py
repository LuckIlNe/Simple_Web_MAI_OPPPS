"""'initial'

Revision ID: 738e6e5c8de3
Revises: 
Create Date: 2022-05-18 20:33:34.540322

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '738e6e5c8de3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('capasity', sa.String(), nullable=False),
    sa.Column('authors', sa.String(), nullable=False),
    sa.Column('categories', postgresql.ARRAY(sa.Enum('Gadgets', 'Weapon', 'Blogs', 'Advertising', 'Transport', 'Jobs', 'Affiliate_material', 'Mathematics', 'IT', 'Astronomy', 'Physics', 'Chemistry', 'Geology', name='categories')), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('articles')
    # ### end Alembic commands ###