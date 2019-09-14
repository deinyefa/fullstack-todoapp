"""empty message

Revision ID: 3fef896f2d92
Revises: 
Create Date: 2019-09-14 09:44:47.440336

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '3fef896f2d92'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    op.execute('UPDATE todos SET completed=False WHERE todos.completed IS NULL;')
    op.alter_column('todos', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###