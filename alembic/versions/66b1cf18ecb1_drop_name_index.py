"""Drop name index

Revision ID: 66b1cf18ecb1
Revises: 6a66d5ab78e5
Create Date: 2022-08-23 16:50:23.238973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66b1cf18ecb1'
down_revision = '6a66d5ab78e5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_name', table_name='user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_user_name', 'user', ['name'], unique=False)
    # ### end Alembic commands ###