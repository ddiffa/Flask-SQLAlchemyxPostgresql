"""empty message

Revision ID: cd8d7304aef4
Revises: 5eab70d11f52
Create Date: 2019-11-05 23:32:29.830293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd8d7304aef4'
down_revision = '5eab70d11f52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('participans', 'fk_ticketid',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('participans', 'status',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('tickets', 'fk_eventid',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('tickets', 'fk_userid',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('tickets', 'ticket_phone')
    op.drop_column('tickets', 'ticket_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickets', sa.Column('ticket_name', sa.VARCHAR(length=400), autoincrement=False, nullable=False))
    op.add_column('tickets', sa.Column('ticket_phone', sa.VARCHAR(length=300), autoincrement=False, nullable=False))
    op.alter_column('tickets', 'fk_userid',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('tickets', 'fk_eventid',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('participans', 'status',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('participans', 'fk_ticketid',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
