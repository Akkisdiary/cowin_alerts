"""update table names

Revision ID: bef49b274d36
Revises: 55c417e0d2cd
Create Date: 2021-06-10 21:42:49.674413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bef49b274d36'
down_revision = '55c417e0d2cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscriber_pincode_preferences')
    op.drop_table('subscribers')

    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.Column('phone', sa.String(length=13), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('phone'),
                    sa.UniqueConstraint('phone')
                    )
    op.create_table('subscriptions',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('subscriber_id', sa.Integer(), nullable=False),
                    sa.Column('pincode_id', sa.Integer(), nullable=False),
                    sa.Column('preference_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['pincode_id'], ['pincodes.id'], ),
                    sa.ForeignKeyConstraint(
                        ['preference_id'], ['preference.id'], ),
                    sa.ForeignKeyConstraint(['subscriber_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint(
                        'subscriber_id', 'pincode_id', 'preference_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscriber_pincode_preferences',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('subscriber_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.Column('pincode_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.Column('preference_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['pincode_id'], [
                        'pincodes.id'], name='subscriber_pincode_preferences_pincode_id_fkey'),
                    sa.ForeignKeyConstraint(['preference_id'], [
                        'preference.id'], name='subscriber_pincode_preferences_preference_id_fkey'),
                    sa.ForeignKeyConstraint(['subscriber_id'], [
                        'subscribers.id'], name='subscriber_pincode_preferences_subscriber_id_fkey'),
                    sa.PrimaryKeyConstraint(
                        'id', name='subscriber_pincode_preferences_pkey'),
                    sa.UniqueConstraint('subscriber_id', 'pincode_id', 'preference_id',
                                        name='subscriber_pincode_preference_subscriber_id_pincode_id_pref_key')
                    )
    op.create_table('subscribers',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('email', sa.VARCHAR(length=512),
                              autoincrement=False, nullable=False),
                    sa.Column('name', sa.VARCHAR(length=64),
                              autoincrement=False, nullable=False),
                    sa.Column('phone', sa.VARCHAR(length=13),
                              autoincrement=False, nullable=True),
                    sa.Column('subscribed', sa.BOOLEAN(),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='subscribers_pkey'),
                    sa.UniqueConstraint('email', name='subscribers_email_key'),
                    sa.UniqueConstraint('phone', name='subscribers_phone_key')
                    )
    op.drop_table('subscriptions')
    op.drop_table('users')
    # ### end Alembic commands ###
