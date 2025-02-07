"""empty message

Revision ID: 54e5dbe5d30f
Revises: f7f4749b4c99
Create Date: 2022-09-09 18:40:57.204865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54e5dbe5d30f'
down_revision = 'f7f4749b4c99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artist', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artist', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    op.alter_column('artist', 'facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artist', 'website_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('venue', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('venue', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    op.alter_column('venue', 'facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('venue', 'website_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venue', 'website_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('venue', 'facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('venue', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.alter_column('venue', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artist', 'website_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artist', 'facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artist', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.alter_column('artist', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###
