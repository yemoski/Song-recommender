"""'drop_artist'

Revision ID: ffd7f4e3908a
Revises: 60bb8c455279
Create Date: 2022-08-26 20:24:28.025432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffd7f4e3908a'
down_revision = '60bb8c455279'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recommendations', 'artist_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recommendations', sa.Column('artist_name', sa.VARCHAR(length=40), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
