"""Initial migration.

Revision ID: 8978f2c9da41
Revises: 
Create Date: 2022-06-12 22:20:55.882028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8978f2c9da41'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    # ### end Alembic commands ###
