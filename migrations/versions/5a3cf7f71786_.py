"""Create 'paricipation' table, which is a relation table between 'meal' and 'friend'

Revision ID: 5a3cf7f71786
Revises: 3a5de6b4bb46
Create Date: 2015-08-22 10:35:36.395198

"""

# revision identifiers, used by Alembic.
revision = '5a3cf7f71786'
down_revision = '3a5de6b4bb46'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('participation',
    sa.Column('friend_id', sa.Integer(), nullable=False),
    sa.Column('meal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['friend_id'], ['friend.id'], name='fk_participation_friend'),
    sa.ForeignKeyConstraint(['meal_id'], ['meal.id'], name='fk_participation_meal'),
    sa.PrimaryKeyConstraint('friend_id', 'meal_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('participation')
    ### end Alembic commands ###
