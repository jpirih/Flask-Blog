"""empty message

Revision ID: e43b20096483
Revises: 4d6cdc2aef74
Create Date: 2016-04-03 17:39:56.315000

"""

# revision identifiers, used by Alembic.
revision = 'e43b20096483'
down_revision = '4d6cdc2aef74'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'posts', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.drop_column(u'users', 'fav_color')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'users', sa.Column('fav_color', mysql.VARCHAR(length=155), nullable=True))
    op.drop_column(u'posts', 'created_at')
    op.drop_table('comments')
    ### end Alembic commands ###
