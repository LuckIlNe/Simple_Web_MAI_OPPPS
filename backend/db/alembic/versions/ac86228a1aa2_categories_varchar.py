"""categories[] -> varchar[]

Revision ID: ac86228a1aa2
Revises: f37b3cd62542
Create Date: 2022-05-20 20:34:37.185422

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ac86228a1aa2'
down_revision = 'f37b3cd62542'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('articles', 'categories',
               existing_type=postgresql.ARRAY(postgresql.ENUM('Gadgets', 'Weapon', 'Blogs', 'Advertising', 'Transport', 'Jobs', 'Affiliate_material', 'Mathematics', 'IT', 'Astronomy', 'Physics', 'Chemistry', 'Geology', name='categories')),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('articles', 'categories',
               existing_type=postgresql.ARRAY(postgresql.ENUM('Gadgets', 'Weapon', 'Blogs', 'Advertising', 'Transport', 'Jobs', 'Affiliate_material', 'Mathematics', 'IT', 'Astronomy', 'Physics', 'Chemistry', 'Geology', name='categories')),
               nullable=True)
    # ### end Alembic commands ###
