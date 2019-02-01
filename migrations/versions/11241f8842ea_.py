"""empty message

Revision ID: 11241f8842ea
Revises: 2b6ffd3f4e8e
Create Date: 2019-02-01 12:24:56.677462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11241f8842ea'
down_revision = '2b6ffd3f4e8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    # ### end Alembic commands ###
