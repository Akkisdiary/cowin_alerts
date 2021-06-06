"""add subscribed column to users table

Revision ID: 55c417e0d2cd
Revises: d3e68f400290
Create Date: 2021-06-06 14:38:13.723688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55c417e0d2cd'
down_revision = 'd3e68f400290'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pincodes', sa.Column('sub_45_last_mail_sent_on', sa.DateTime(), nullable=True))
    op.add_column('subscribers', sa.Column('subscribed', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subscribers', 'subscribed')
    op.drop_column('pincodes', 'sub_45_last_mail_sent_on')
    # ### end Alembic commands ###
