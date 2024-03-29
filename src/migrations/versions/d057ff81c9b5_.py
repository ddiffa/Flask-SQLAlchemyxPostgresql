"""empty message

Revision ID: d057ff81c9b5
Revises: 26b596bcbb1c
Create Date: 2019-11-06 02:21:44.104464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd057ff81c9b5'
down_revision = '26b596bcbb1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'tickets_participan_id_fkey', 'tickets', type_='foreignkey')
    op.drop_column('tickets', 'participan_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickets', sa.Column('participan_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'tickets_participan_id_fkey', 'tickets', 'participans', ['participan_id'], ['id'])
    # ### end Alembic commands ###
