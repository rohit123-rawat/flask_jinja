"""Added role column in user

Revision ID: 34fc5d0e48fc
Revises: 47fa5e8afe44
Create Date: 2023-07-24 15:28:37.228261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34fc5d0e48fc'
down_revision = '47fa5e8afe44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('role', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###