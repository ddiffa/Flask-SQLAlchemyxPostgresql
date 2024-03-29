"""empty message

Revision ID: a156dbc5392b
Revises: 
Create Date: 2019-11-05 00:45:07.873548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a156dbc5392b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.String(length=128), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fk_userid', sa.Integer(), nullable=True),
    sa.Column('event_name', sa.String(length=400), nullable=False),
    sa.Column('event_date', sa.DateTime(), nullable=True),
    sa.Column('event_place', sa.String(length=300), nullable=False),
    sa.Column('event_detail', sa.String(length=500), nullable=False),
    sa.Column('event_image', sa.String(length=250), nullable=False),
    sa.Column('event_category', sa.String(length=100), nullable=False),
    sa.Column('event_talent', sa.String(length=200), nullable=False),
    sa.Column('event_quota', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fk_userid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tickets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fk_userid', sa.Integer(), nullable=True),
    sa.Column('fk_eventid', sa.Integer(), nullable=True),
    sa.Column('ticket_name', sa.String(length=400), nullable=False),
    sa.Column('ticket_phone', sa.String(length=300), nullable=False),
    sa.Column('ticket_qtys', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fk_eventid'], ['events.id'], ),
    sa.ForeignKeyConstraint(['fk_userid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tickets')
    op.drop_table('events')
    op.drop_table('users')
    # ### end Alembic commands ###
